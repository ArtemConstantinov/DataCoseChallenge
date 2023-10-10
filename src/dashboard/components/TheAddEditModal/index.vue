<template>
    <b-modal 
        :visible="show" 
        @hide="(v) => $emit('hide', v)"
        :title="title"
        centered
    >   
        <slot></slot>
        <template #modal-footer>
            <component 
                :is="footer_component" 
                v-on="$listeners"
            />
        </template>
    </b-modal>
</template>

<script>
import TheAddFooter from "./TheAddFooter.vue";
import TheEditFooter from "./TheEditFooter.vue";

export default {
    name: "TheAddEditModal",
    components: {
        TheAddFooter,
        TheEditFooter
    },
    props: {
        addTitle: {
            type: String,
            default: "Add New"
        },
        editTitle: {
            type: String,
            default: "Edit"
        },
        show: {
            type: Boolean,
            default: false
        },
        edit: {
            type: Boolean,
            default: false
        },
    },
    computed: {
        title() {
            return this.edit? this.editTitle : this.addTitle;
        },
        footer_component() {
            return this.edit? "TheEditFooter" : "TheAddFooter";
        },
    }
}
</script>

<style lang="scss" scoped>
.actions-container
{
    display: grid;
    justify-items: end;
    margin-top: 2.5rem;
}
</style>