// File: netlify/functions/submit-contact.js

// Proxy contact form submissions to n8n to avoid CORS issues and hide the webhook URL

const WEBHOOK_URL = process.env.N8N_WEBHOOK_URL || 'https://n8n.ssilva.space/webhook/31d9264e-2d99-4c75-bbd8-eb86c0ede5ee';

function corsHeaders() {
	return {
		'Access-Control-Allow-Origin': '*',
		'Access-Control-Allow-Methods': 'POST, OPTIONS',
		'Access-Control-Allow-Headers': 'Content-Type',
		'Access-Control-Max-Age': '86400'
	};
}

exports.handler = async function(event) {
	// Handle CORS preflight
	if (event.httpMethod === 'OPTIONS') {
		return {
			statusCode: 200,
			headers: corsHeaders(),
			body: ''
		};
	}

	if (event.httpMethod !== 'POST') {
		return { statusCode: 405, headers: corsHeaders(), body: 'Method Not Allowed' };
	}

	try {
		const contentType = event.headers['content-type'] || event.headers['Content-Type'] || '';
		if (!contentType.includes('application/json')) {
			return { statusCode: 400, headers: corsHeaders(), body: 'Bad Request: expected application/json' };
		}

		const payload = JSON.parse(event.body || '{}');

		// Basic validation
		if (!payload.name || !payload.email || !payload.message) {
			return { statusCode: 400, headers: corsHeaders(), body: 'Missing required fields: name, email, message' };
		}

		// Enrich with server timestamp and source if missing
		const forwarded = {
			...payload,
			server_timestamp: new Date().toISOString(),
			via: 'netlify-function-proxy'
		};

		// Forward to n8n webhook
		const response = await fetch(WEBHOOK_URL, {
			method: 'POST',
			headers: { 'Content-Type': 'application/json' },
			body: JSON.stringify(forwarded)
		});

		if (!response.ok) {
			const text = await response.text().catch(() => '');
			return {
				statusCode: 502,
				headers: corsHeaders(),
				body: JSON.stringify({ error: 'Upstream webhook error', status: response.status, body: text })
			};
		}

		return {
			statusCode: 200,
			headers: corsHeaders(),
			body: JSON.stringify({ ok: true })
		};
	} catch (err) {
		return {
			statusCode: 500,
			headers: corsHeaders(),
			body: JSON.stringify({ error: 'Server error', message: err && err.message ? err.message : String(err) })
		};
	}
};

