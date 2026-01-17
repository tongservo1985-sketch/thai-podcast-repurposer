/** @type {import('next-sitemap').IConfig} */
module.exports = {
  siteUrl: 'https://overlord.ai',
  generateRobotsTxt: true,
  exclude: ['/dashboard', '/dashboard/*', '/settings'],
  transform: async (config, path) => {
    // Custom logic to prioritize Thai content paths
    return {
      loc: path,
      changefreq: config.changefreq,
      priority: path === '/' ? 1.0 : 0.7,
      lastmod: config.autoLastmod ? new Date().toISOString() : undefined,
      alternateRefs: [
        {
          href: 'https://overlord.ai/th',
          hreflang: 'th',
        },
      ],
    }
  },
}