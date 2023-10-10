export default {
    // Disable telemetry
    telemetry: false,
    // Configure file watcher
    watchers: {
        webpack: {
            poll: true
        }
    },
    // Disable server-side rendering: https://go.nuxtjs.dev/ssr-mode
    ssr: false,

    // Target: https://go.nuxtjs.dev/config-target
    target: "static",

    // Global page headers: https://go.nuxtjs.dev/config-head
    head: {
        title: "DC Full Stack Code Challenge",
        htmlAttrs: {
            lang: "en",
        },
        meta: [
            { charset: "utf-8" },
            {
                name: "viewport",
                content: "width=device-width, initial-scale=1",
            },
            { hid: "description", name: "description", content: "" },
            { name: "format-detection", content: "telephone=no" },
        ],
        link: [{ rel: "icon", type: "image/x-icon", href: "/favicon.ico" }],
    },

    // Global CSS: https://go.nuxtjs.dev/config-css
    css: [
        "@mdi/font/css/materialdesignicons.css",
        "~/assets/styles/custom.css"
    ],

    // Plugins to run before rendering page: https://go.nuxtjs.dev/config-plugins
    plugins: [],

    // Auto import components: https://go.nuxtjs.dev/config-components
    components: true,

    // Modules for dev and build (recommended): https://go.nuxtjs.dev/config-modules
    buildModules: [
        // https://go.nuxtjs.dev/typescript
        "@nuxt/typescript-build",
    ],

    // Modules: https://go.nuxtjs.dev/config-modules
    modules: [
        // https://go.nuxtjs.dev/bootstrap
        ["bootstrap-vue/nuxt", { icons: true, css: true }],
        // https://go.nuxtjs.dev/axios
        "@nuxtjs/axios",
        "@nuxtjs/auth-next",
    ],

    publicRuntimeConfig: {
        axios: {
            baseURL: process.env.BASEURL || "http://127.0.0.1:8000",
        },
    },

    // Axios module configuration: https://go.nuxtjs.dev/config-axios
    axios: {
        // Workaround to avoid enforcing hard-coded localhost:3000: https://github.com/nuxt-community/axios-module/issues/308
        baseURL: process.env.NODE_ENV == "development" ? "http://127.0.0.1:8000" : process.env.BASEURL,
    },
    auth: {
        strategies: {
            local: {
                token: {
                    property: "access_token",
                    global: true,
                    required: true,
                    type: "Bearer",
                    maxAge: 604800 // 7 days
                },
                endpoints: {
                    login: { url: "/auth/login", method: "post" },
                    logout: { url: "/auth/logout", method: "delete" },
                    user: false
                }
            }
        }
    },

    // Build Configuration: https://go.nuxtjs.dev/config-build
    build: {},
};
