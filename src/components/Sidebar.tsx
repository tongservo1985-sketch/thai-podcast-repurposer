"use client";
import Link from 'next/link';
import { usePathname } from 'next/navigation';
import { 
  LayoutDashboard, 
  Mic2, 
  FileAudio, 
  Settings, 
  Sparkles,
  CreditCard
} from 'lucide-react';
import { cn } from '@/lib/utils';

const navItems = [
  { name: 'Dashboard', href: '/', icon: LayoutDashboard },
  { name: 'Episodes', href: '/episodes', icon: Mic2 },
  { name: 'Library', href: '/library', icon: FileAudio },
  { name: 'AI Settings', href: '/settings/ai', icon: Sparkles },
  { name: 'Billing', href: '/billing', icon: CreditCard },
];

export default function Sidebar() {
  const pathname = usePathname();

  return (
    <aside className="hidden md:flex flex-col w-64 bg-card border-r border-card-border">
      <div className="p-6">
        <h1 className="text-2xl font-bold bg-gradient-to-r from-primary to-purple-400 bg-clip-text text-transparent">
          OVERLORD
        </h1>
        <p className="text-xs text-zinc-500 mt-1 uppercase tracking-widest font-semibold">Thai Podcast AI</p>
      </div>

      <nav className="flex-1 px-4 space-y-2">
        {navItems.map((item) => {
          const Icon = item.icon;
          const isActive = pathname === item.href;
          return (
            <Link
              key={item.href}
              href={item.href}
              className={cn(
                "flex items-center gap-3 px-4 py-3 rounded-lg transition-colors group",
                isActive 
                  ? "bg-primary/10 text-primary" 
                  : "text-zinc-400 hover:bg-zinc-800 hover:text-white"
              )}
            >
              <Icon size={20} className={cn(isActive ? "text-primary" : "group-hover:text-white")} />
              <span className="font-medium">{item.name}</span>
            </Link>
          );
        })}
      </nav>

      <div className="p-4 border-t border-card-border">
        <div className="bg-zinc-900 rounded-lg p-4">
          <p className="text-xs text-zinc-400 mb-2">Usage Credits</p>
          <div className="w-full bg-zinc-800 h-2 rounded-full overflow-hidden">
            <div className="bg-primary w-[65%] h-full" />
          </div>
          <p className="text-[10px] text-zinc-500 mt-2 text-right">130 / 200 mins</p>
        </div>
      </div>
    </aside>
  );
}