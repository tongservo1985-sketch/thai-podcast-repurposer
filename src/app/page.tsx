import { Plus, Upload, Play, CheckCircle2, Clock } from 'lucide-react';

export default function Dashboard() {
  return (
    <div className="space-y-8 animate-in fade-in duration-500">
      <div className="flex items-end justify-between">
        <div>
          <h2 className="text-3xl font-bold">แผงควบคุม (Dashboard)</h2>
          <p className="text-zinc-400 mt-1">ยินดีต้อนรับกลับ, พร้อมสร้างคอนเทนต์ใหม่หรือยัง?</p>
        </div>
        <button className="bg-primary hover:bg-primary/90 text-white px-6 py-3 rounded-xl font-bold flex items-center gap-2 transition-all transform hover:scale-105 active:scale-95 shadow-lg shadow-primary/20">
          <Plus size={20} />
          <span>สร้าง Episode ใหม่</span>
        </button>
      </div>

      {/* Stats Quick View */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        {[
          { label: 'Total Episodes', value: '24', icon: Play, color: 'text-blue-400' },
          { label: 'Minutes Processed', value: '1,240', icon: Clock, color: 'text-purple-400' },
          { label: 'Content Generated', value: '156', icon: CheckCircle2, color: 'text-emerald-400' },
        ].map((stat, i) => (
          <div key={i} className="glass-panel p-6 flex items-center gap-4">
            <div className={`p-3 rounded-lg bg-zinc-900 ${stat.color}`}>
              <stat.icon size={24} />
            </div>
            <div>
              <p className="text-sm text-zinc-500 font-medium">{stat.label}</p>
              <p className="text-2xl font-bold">{stat.value}</p>
            </div>
          </div>
        ))}
      </div>

      {/* Upload Dropzone Placeholder */}
      <div className="glass-panel border-dashed border-2 border-zinc-800 p-12 flex flex-col items-center justify-center text-center space-y-4 hover:border-primary/50 transition-colors cursor-pointer group">
        <div className="p-4 rounded-full bg-primary/10 text-primary group-hover:scale-110 transition-transform">
          <Upload size={32} />
        </div>
        <div>
          <h3 className="text-lg font-semibold">ลากและวางไฟล์เสียงพอดแคสต์ที่นี่</h3>
          <p className="text-zinc-500 text-sm max-w-xs mx-auto mt-2">
            รองรับ MP3, WAV, M4A (สูงสุด 500MB) เพื่อให้ AI เริ่มถอดความและสร้างโซเชียลโพสต์
          </p>
        </div>
      </div>

      {/* Recent Activity Table */}
      <div className="space-y-4">
        <h3 className="text-xl font-semibold">รายการล่าสุด</h3>
        <div className="glass-panel overflow-hidden">
          <table className="w-full text-left border-collapse">
            <thead>
              <tr className="border-b border-card-border bg-zinc-900/50">
                <th className="px-6 py-4 text-xs font-semibold text-zinc-500 uppercase">Episode Name</th>
                <th className="px-6 py-4 text-xs font-semibold text-zinc-500 uppercase">Status</th>
                <th className="px-6 py-4 text-xs font-semibold text-zinc-500 uppercase">Duration</th>
                <th className="px-6 py-4 text-xs font-semibold text-zinc-500 uppercase">Created</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-card-border">
              {[
                { name: 'EP 42: อนาคตของ AI ในไทย', status: 'Completed', time: '45:20', date: '2 hours ago' },
                { name: 'EP 41: การตลาด 5.0 สำหรับ SMEs', status: 'Processing', time: '38:15', date: 'Yesterday' },
                { name: 'EP 40: สัมภาษณ์พิเศษ Tech Founder', status: 'Completed', time: '52:00', date: 'Oct 24, 2023' },
              ].map((row, i) => (
                <tr key={i} className="hover:bg-zinc-800/50 transition-colors cursor-pointer group">
                  <td className="px-6 py-4 font-medium group-hover:text-primary transition-colors">{row.name}</td>
                  <td className="px-6 py-4">
                    <span className={cn(
                      "px-2 py-1 rounded-full text-[10px] font-bold uppercase tracking-wider",
                      row.status === 'Completed' ? "bg-emerald-500/10 text-emerald-500" : "bg-amber-500/10 text-amber-500 animate-pulse"
                    )}>
                      {row.status}
                    </span>
                  </td>
                  <td className="px-6 py-4 text-zinc-400 text-sm">{row.time}</td>
                  <td className="px-6 py-4 text-zinc-500 text-sm">{row.date}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}