

import 'animate.css';
import DashboardData from '../components/DashboardData';

export default function Home() {
  return (
    <div className="min-h-screen font-sans" style={{
      background: 'radial-gradient(circle at top right, #1e1b4b, #0f172a)',
      color: 'white',
      overflowX: 'hidden',
      fontFamily: 'Inter, sans-serif',
    }}>
      {/* Navbar */}
      <nav className="flex justify-between items-center p-6 max-w-7xl mx-auto animate__animated animate__fadeInDown">
        <div className="text-2xl font-extrabold tracking-tighter">FIN<span className="text-indigo-500">SENSE</span></div>
        <div className="hidden md:flex space-x-8 text-sm font-medium opacity-80">
          <a href="#" className="hover:text-indigo-400 transition">Product</a>
          <a href="#" className="hover:text-indigo-400 transition">Security</a>
          <a href="#" className="hover:text-indigo-400 transition">Pricing</a>
        </div>
        <button className="bg-indigo-600 hover:bg-indigo-500 px-6 py-2 rounded-full font-semibold transition-all">Get Started</button>
      </nav>


      {/* Main Hero Section */}
      <main className="max-w-7xl mx-auto px-6 pt-20 pb-12 text-center">
        <h1 className="text-5xl md:text-8xl font-extrabold mb-6 animate__animated animate__zoomIn">
          Stop Tracking. <br /> <span className="gradient-text" style={{
            background: 'linear-gradient(90deg, #818cf8, #c084fc)',
            WebkitBackgroundClip: 'text',
            WebkitTextFillColor: 'transparent',
            display: 'inline-block',
          }}>Start Growing.</span>
        </h1>
        <p className="text-lg md:text-xl text-slate-400 max-w-2xl mx-auto mb-10 animate__animated animate__fadeInUp animate__delay-1s">
          The first AI-native finance coach that talks to you like a human and thinks like a hedge fund manager.
        </p>
        <div className="flex flex-col md:flex-row justify-center gap-4 animate__animated animate__fadeInUp animate__delay-1s">
          <button className="bg-white text-black px-8 py-4 rounded-xl font-bold hover:scale-105 transition-transform">Download App</button>
          <button className="glass-card px-8 py-4 rounded-xl font-bold hover:scale-105 transition-transform" style={{
            background: 'rgba(255,255,255,0.03)',
            backdropFilter: 'blur(12px)',
            border: '1px solid rgba(255,255,255,0.1)',
            transition: 'transform 0.3s ease, box-shadow 0.3s ease',
          }}>View Demo</button>
        </div>
      </main>

      {/* Dashboard Data Section (Live from backend) */}
      <DashboardData />

      {/* Features Section */}
      <section className="max-w-7xl mx-auto px-6 py-20 grid grid-cols-1 md:grid-cols-3 gap-8">
        <div className="glass-card p-8 rounded-2xl" style={{
          background: 'rgba(255,255,255,0.03)',
          backdropFilter: 'blur(12px)',
          border: '1px solid rgba(255,255,255,0.1)',
          transition: 'transform 0.3s ease, box-shadow 0.3s ease',
        }}>
          <div className="text-3xl mb-4">🤖</div>
          <h3 className="text-xl font-bold mb-2">AI Coaching</h3>
          <p className="text-slate-400 text-sm">Real-time voice and text guidance to help you make better spending decisions on the fly.</p>
        </div>
        <div className="glass-card p-8 rounded-2xl" style={{
          background: 'rgba(255,255,255,0.03)',
          backdropFilter: 'blur(12px)',
          border: '1px solid rgba(255,255,255,0.1)',
          transition: 'transform 0.3s ease, box-shadow 0.3s ease',
        }}>
          <div className="text-3xl mb-4">🔒</div>
          <h3 className="text-xl font-bold mb-2">Bank-Level Security</h3>
          <p className="text-slate-400 text-sm">We use 256-bit AES encryption. Your data is yours. We never see your login credentials.</p>
        </div>
        <div className="glass-card p-8 rounded-2xl" style={{
          background: 'rgba(255,255,255,0.03)',
          backdropFilter: 'blur(12px)',
          border: '1px solid rgba(255,255,255,0.1)',
          transition: 'transform 0.3s ease, box-shadow 0.3s ease',
        }}>
          <div className="text-3xl mb-4">📊</div>
          <h3 className="text-xl font-bold mb-2">Smart Insights</h3>
          <p className="text-slate-400 text-sm">Visualizations that actually make sense. No more digging through confusing spreadsheets.</p>
        </div>
      </section>
    </div>
  );
}
