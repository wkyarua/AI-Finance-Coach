// Utility to get backend API URL
export function getBackendUrl() {
  // Use environment variable or fallback to localhost
  return process.env.NEXT_PUBLIC_BACKEND_URL || 'http://localhost:8000';
}
