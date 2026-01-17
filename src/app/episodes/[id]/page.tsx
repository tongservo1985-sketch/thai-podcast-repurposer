"use client";
import { ChevronLeft, Share2, Copy, Facebook, MessageSquare, Video } from 'lucide-react';
import Link from 'next/link';

export default function EpisodeDetail({ params }: { params: { id: string } }) {
  // Mock data for UI demonstration
  const episode = {
    title: "EP 42: อนาคตของ AI ในไทย",
    status: "Completed",
    content: {
      facebook: "สรุปประเด็นร้อนจากพอดแคสต์ล่าสุด! 🔥\n\nทำไม AI ถึงจะเข้ามาเปลี่ยนโฉมธุรกิจไทยในปี 2024...\n1. การประมวลผลภาษาไทยที่เก่งขึ้น\n2. การลดต้นทุนในสายงาน Creative\n3. SMEs ต้องปรับตัวอย่างไร?\n\nฟังเต็มๆ ได้ที่ลิงก์ในคอมเมนต์! 👇 #AI #Thailand #TechTrend",
      threads: "AI ในไทยไปถึงไหนแล้ว? 🇹🇭 จากพอดแคสต์ล่าสุด สรุปสั้นๆ คือเรากำลังก้าวเข้าสู่ยุค 'Hyper-Localization' ที่ภาษาไทยจะไม่เป็นอุปสรรคอีกต่อไป...",
      tiktok: "สคริปต์วิดีโอ 30 วินาที:\n(0:00) 'รู้ไหมว่า AI ภาษาไทยตอนนี้เก่งขึ้น 10 เท่า?'\n(0:05) 'จากงานวิจัยล่าสุดบอกว่า...'"
    }
  };

  return (
    <div className="space-y-6 max-w-5xl mx-auto">
      <Link href="/" className="flex items-center gap-2 text-zinc-400 hover:text-white transition-colors">
        <ChevronLeft size={20} />
        <span>กลับไปที่รายการทั้งหมด</span>
      </Link>

      <div className="flex flex-col md:flex-row md:items-center justify-between gap-4">
        <h1 className="text-3xl font-bold">{episode.title}</h1>
        <div className="flex gap-2">
          <button className="glass-panel px-4 py-2 flex items-center gap-2 hover:bg-zinc-800 transition-colors">
            <Share2 size={18} />
            <span>Share</span>
          </button>
        </div>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        {/* Transcription Preview */}
        <div className="lg:col-span-2 space-y-6">
          <div className="glass-panel p-6 h-[600px] flex flex-col">
            <h3 className="font-semibold mb-4 flex items-center gap-2">
              <MessageSquare size={18} className="text-primary" />
              บทบรรยาย (Transcript)
            </h3>
            <div className="flex-1 overflow-y-auto pr-4 space-y-4 text-zinc-300 leading-relaxed">
              <p><span className="text-primary font-mono text-xs mr-2">[00:00]</span> สวัสดีครับยินดีต้อนรับเข้าสู่พอดแคสต์ของเรานะครับ วันนี้เราจะมาคุยกันเรื่องที่น่าสนใจมาก...</p>
              <p><span className="text-primary font-mono text-xs mr-2">[01:15]</span> ในช่วงปีที่ผ่านมา เราเห็นการเติบโตของ Large Language Models ที่รองรับภาษาไทยได้ดีขึ้นอย่างก้าวกระโดด...</p>
              <p><span className="text-zinc-500 italic">...และอีกมากมายที่ AI ถอดความให้คุณ...</span></p>
            </div>
          </div>
        </div>

        {/* AI Transformation Cards */}
        <div className="space-y-4">
          <h3 className="font-semibold px-2">Social Media Transformation</h3>
          
          {/* Facebook Card */}
          <div className="glass-panel p-4 space-y-3 relative group">
            <div className="flex items-center justify-between">
              <div className="flex items-center gap-2 text-blue-500 font-bold">
                <Facebook size={18} />
                <span>Facebook Post</span>
              </div>
              <button className="text-zinc-500 hover:text-white"><Copy size={16} /></button>
            </div>
            <p className="text-sm text-zinc-300 whitespace-pre-wrap line-clamp-6">
              {episode.content.facebook}
            </p>
            <div className="pt-2 border-t border-card-border flex justify-end">
              <button className="text-xs text-primary font-bold hover:underline">Edit Content</button>
            </div>
          </div>

          {/* TikTok Card */}
          <div className="glass-panel p-4 space-y-3 relative group">
            <div className="flex items-center justify-between">
              <div className="flex items-center gap-2 text-pink-500 font-bold">
                <Video size={18} />
                <span>TikTok Script</span>
              </div>
              <button className="text-zinc-500 hover:text-white"><Copy size={16} /></button>
            </div>
            <p className="text-sm text-zinc-300 whitespace-pre-wrap">
              {episode.content.tiktok}
            </p>
          </div>
        </div>
      </div>
    </div>
  );
}