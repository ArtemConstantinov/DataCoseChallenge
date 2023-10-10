<template>
    <div>
        <TheNavBar />
        <b-container class="mt-7">
            <b-row>
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
}
</script>

<style>
th, td
{
    vertical-align: middle !important;
}
</style>

