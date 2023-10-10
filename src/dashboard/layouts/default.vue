<template>
    <div>
        <TheNavBar />
        <b-container class="mt-7">
            <b-row>
                <!-- <b-col xl="12" class="mb-5 mb-xl-0">
                    <b-breadcrumb :items="items"></b-breadcrumb>
                </b-col> -->
                <b-col xl="12" class="mb-5 mb-xl-0">
                    <nuxt />
                </b-col>
            </b-row>
        </b-container>
    </div>
</template>

<script>
import TheNavBar from '~/components/TheNavBar.vue';
export default {
    name: "base-layout",
    middleware: "auth",
    // computed: {
    //     title(ctx) {
    //         return ctx.$root.$meta().refresh().metaInfo.titleChunk
    //     },
    //     items() {
    //         return [
    //             {
    //                 text: this.title,
    //                 href: '#'
    //             },
    //             {
    //                 text: 'Manage',
    //                 href: '#'
    //             },
    //             {
    //                 text: 'Library',
    //                 active: true
    //             }
    //         ]
    //     }
    // }

}
</script>

<style>
th, td
{
    vertical-align: middle !important;
}
</style>

