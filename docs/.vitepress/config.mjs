import { defineConfig } from "vitepress";

// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: "Bangla Programming Resources",
  description:
    "Bangla tutorial, reference and resource list on programming topics",
  themeConfig: {
    // https://vitepress.dev/reference/default-theme-config
    siteTitle: "বাংলায় প্রোগ্রামিং রিসোর্সসমূহ",
    nav: [
      { text: "হোমপেজ", link: "/" },
      { text: "রিসোর্সসমূহ", link: "/resources" },
      { text: "কন্ট্রিবিউটর", link: "/contributors" },
    ],

    sidebar: [
      {
        text: "রিসোর্সসমূহ",
        link: "/resources",
      },
    ],

    socialLinks: [
      {
        icon: "github",
        link: "https://github.com/me-shaon/bangla-programming-resources",
      },
    ],
  },
});
