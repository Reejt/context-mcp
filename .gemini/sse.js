import EventSource from 'eventsource';
const es = new EventSource('http://localhost:4333/events');

es.onmessage = function(event) {
  console.log('Received event:', event.data);
};

es.onerror = function(err) {
  console.error('SSE error:', err);
};