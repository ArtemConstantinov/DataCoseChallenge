<template>
    <div class="w-100 edit-actions">
        <b-button @click="onDelete" variant="danger">
            <span class="mdi mdi-delete-outline" style="margin-right: 0.4rem;"></span>
            Delete
        </b-button>
        <b-button @click="onSubmit" variant="primary">
            <span class="mdi mdi-content-save-outline" style="margin-right: 0.4rem;"></span>
            Save
        </b-button>
    </div>
</template>

<script>
export default {
    methods: {
        onSubmit() {
            this.$emit("on-edit");
        },
        onDelete() {
            this.$emit("on-delete");
        },
    }
}
</script>

<style lang="scss" scoped>
.edit-actions
{
    display: flex;
    justify-content: flex-end;
    gap: 1rem;
    max-height: 40px;
}
</style>