<template>
    <b-navbar toggleable="lg" variant="light" small>
        <b-nav-text>Click on the rows you want to modify.</b-nav-text>
        <b-navbar-nav class="ml-auto">
            <b-button 
                size="sm"
                @click="() => $emit('on-add')" 
                variant="primary"
                v-b-tooltip.hover
                delay="500"
                title="Add book" 
                class="float-right"
            >
                <span class="mdi mdi-plus"></span>
            </b-button>
        </b-navbar-nav> 
    </b-navbar>
</template>

<script>
export default {}
</script>