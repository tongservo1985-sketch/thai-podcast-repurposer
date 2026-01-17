import Head from 'next/head';

interface SEOProps {
  title?: string;
  description?: string;
  ogImage?: string;
  canonicalUrl?: string;
}

/**
 * SEO Component optimized for Thai Social Media Sharing (OpenGraph)
 * Ensures Thai characters and emojis are rendered correctly in previews.
 */
export default function SEO({ 
  title = "OVERLORD - AI ผู้ช่วยอัจฉริยะสำหรับนักจัดพอดแคสต์ไทย",
  description = "เปลี่ยนพอดแคสต์ของคุณเป็นคอนเทนต์โซเชียลมีเดียที่น่าดึงดูดในคลิกเดียว ด้วย AI ที่เข้าใจภาษาไทยที่สุด",
  ogImage = "https://overlord.ai/og-image-thai.png",
  canonicalUrl = "https://overlord.ai"
}: SEOProps) {
  const siteName = "OVERLORD AI";

  return (
    <Head>
      <title>{title}</title>
      <meta name="description" content={description} />
      <meta name="viewport" content="width=device-width, initial-scale=1" />
      <meta charSet="utf-8" />
      
      {/* Open Graph / Facebook */}
      <meta property="og:type" content="website" />
      <meta property="og:url" content={canonicalUrl} />
      <meta property="og:title" content={title} />
      <meta property="og:description" content={description} />
      <meta property="og:image" content={ogImage} />
      <meta property="og:site_name" content={siteName} />
      <meta property="og:locale" content="th_TH" />

      {/* Twitter */}
      <meta property="twitter:card" content="summary_large_image" />
      <meta property="twitter:url" content={canonicalUrl} />
      <meta property="twitter:title" content={title} />
      <meta property="twitter:description" content={description} />
      <meta property="twitter:image" content={ogImage} />

      <link rel="canonical" href={canonicalUrl} />
      
      {/* Favicon */}
      <link rel="icon" href="/favicon.ico" />
    </Head>
  );
}