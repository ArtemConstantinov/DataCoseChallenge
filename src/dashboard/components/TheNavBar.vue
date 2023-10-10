<template>
    <b-navbar toggleable="lg" type="dark" variant="dark">
        <b-navbar-nav class="mr-auto">
            <b-nav-item 
                v-for="item in menu"
                :key="item.title"
                :to="item.path" 
                :active="path === item.path"
            >
                {{ item.title }}
            </b-nav-item>
        </b-navbar-nav>
        <b-navbar-nav class="ml-auto">
            <b-nav-item 
                v-b-tooltip.hover
                delay="500"
                title="Logout"    
                @click="doLogout"
            >
                <span class="mdi mdi-logout" style="font-size: 1.3rem;"></span>
            </b-nav-item>
        </b-navbar-nav>
    </b-navbar>
</template>

<script>
export default {
    data() {
        return {
            menu: [
                {
                    title: "Authors",
                    path: "/",
                },
                {
                    title: "Books",
                    path: "/books",
                }
            ]
        }
    },
    computed: {
        path() {
            return this.$nuxt.$route.path;
        }
    },
    methods: {
        async doLogout() {
            await this.$auth.logout();
            this.$nuxt.$router.push('/login');
        }
        
    },
}
</script>

<style scoped>
.btn-logout 
{
    color: var(--danger) !important;
}
</style>