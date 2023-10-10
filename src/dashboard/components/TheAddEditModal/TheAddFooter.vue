<template>
    <div class="w-100">
        <b-button @click="onSubmit" variant="primary" class="float-right">
            <span class="mdi mdi-content-save-outline" style="margin-right: 0.4rem;"></span>
            Save
        </b-button>
    </div>
</template>

<script>
export default {
    methods: {
        onSubmit() {
            this.$emit("on-create-new", null);
        }
    }
}
</script>