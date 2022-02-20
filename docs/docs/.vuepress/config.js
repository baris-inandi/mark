// TODO: add google analytics
// https://v2.vuepress.vuejs.org/reference/plugin/google-analytics.html#install

module.exports = {
    lang: "en-US",
    title: "Mark Documentation",
    description: "Documentation for the Mark language.",
    sidebar: [{ "Getting Started": "gettingStarted/" }],
    plugins: [
        [
            "@vuepress/search",
            {
                searchMaxSuggestions: 10,
            },
        ],
    ],
    theme: "@vuepress/theme-default",
    themeConfig: {
        logo: "https://vuejs.org/images/logo.png",
        nav: [{ text: "GitHub", link: "https://github.com/baris-inandi/mark" }],
        themeConfig: {
            sidebar: {
                // . . .
            },
            sidebarDepth: 2,
        },
    },
};
