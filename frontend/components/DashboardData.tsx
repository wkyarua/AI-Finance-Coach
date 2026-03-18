"use client";
import { useEffect, useState } from 'react';
import { fetchAnalytics, fetchTrends, fetchForecast } from './api';

export default function DashboardData() {
  const [analytics, setAnalytics] = useState<any[]>([]);
  const [trends, setTrends] = useState<any[]>([]);
  const [forecast, setForecast] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    async function loadData() {
      try {
        setLoading(true);
        const [a, t, f] = await Promise.all([
          fetchAnalytics(),
          fetchTrends(),
          fetchForecast()
        ]);
        setAnalytics(a);
        setTrends(t);
        setForecast(f);
      } catch (e: any) {
        setError(e.message || 'Failed to load data');
      } finally {
        setLoading(false);
      }
    }
    loadData();
  }, []);

  if (loading) return <div className="text-center py-8">Loading dashboard data...</div>;
  if (error) return <div className="text-center text-red-500 py-8">{error}</div>;

  return (
    <div className="max-w-4xl mx-auto my-8 p-6 bg-white/5 rounded-xl">
      <h2 className="text-2xl font-bold mb-4">Analytics</h2>
      <ul className="mb-6">
        {analytics.map((a, i) => (
          <li key={i} className="flex justify-between border-b border-white/10 py-2">
            <span>{a.category}</span>
            <span className="font-mono">${a.total.toFixed(2)}</span>
          </li>
        ))}
      </ul>
      <h2 className="text-2xl font-bold mb-4">Trends</h2>
      <ul className="mb-6">
        {trends.map((t, i) => (
          <li key={i} className="flex justify-between border-b border-white/10 py-2">
            <span>{t.category}</span>
            <span>{t.trend} ({t.change >= 0 ? '+' : ''}{t.change.toFixed(2)})</span>
          </li>
        ))}
      </ul>
      <h2 className="text-2xl font-bold mb-4">Forecast</h2>
      {forecast && (
        <div className="flex flex-col md:flex-row gap-4">
          <div className="flex-1 bg-indigo-500/10 p-4 rounded-lg">
            <div className="text-slate-400 text-sm">Estimated Balance</div>
            <div className="text-3xl font-bold">${forecast.estimated_balance.toFixed(2)}</div>
          </div>
          <div className="flex-1 bg-indigo-500/10 p-4 rounded-lg">
            <div className="text-slate-400 text-sm">Recurring Expenses</div>
            <div className="text-3xl font-bold">${forecast.recurring_expenses.toFixed(2)}</div>
          </div>
        </div>
      )}
    </div>
  );
}
