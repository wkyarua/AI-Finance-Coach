import { getBackendUrl } from '../utils';

export async function fetchCategories() {
  const res = await fetch(`${getBackendUrl()}/categories`);
  if (!res.ok) throw new Error('Failed to fetch categories');
  return res.json();
}

export async function fetchTransactions() {
  const res = await fetch(`${getBackendUrl()}/transactions`);
  if (!res.ok) throw new Error('Failed to fetch transactions');
  return res.json();
}

export async function fetchAnalytics() {
  const res = await fetch(`${getBackendUrl()}/analytics`);
  if (!res.ok) throw new Error('Failed to fetch analytics');
  return res.json();
}

export async function fetchTrends() {
  const res = await fetch(`${getBackendUrl()}/trends`);
  if (!res.ok) throw new Error('Failed to fetch trends');
  return res.json();
}

export async function fetchForecast() {
  const res = await fetch(`${getBackendUrl()}/forecast`);
  if (!res.ok) throw new Error('Failed to fetch forecast');
  return res.json();
}
