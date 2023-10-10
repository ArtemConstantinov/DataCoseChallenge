<template>
    <main>
        <nuxt />
    </main>
</template>

<script>
export default {
    name: "layout-initial",
    middleware: "auth",

}
</script>

<style lang="scss" scoped>
main {
    width: 100vw;
    height: 100vh;
    overflow: hidden;
    display: flex;
    align-items: center;
    justify-content: center;
}
</style>