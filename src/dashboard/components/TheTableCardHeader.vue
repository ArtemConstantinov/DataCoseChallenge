<template>
    <b-nav card-header>
        <b-navbar-nav>
            <b-input-group>
                <b-form-input
                    :value="value"
                    @input="(e) => $emit('input', e)"
                    type="search"
                    placeholder="Type to Search"
                    style="min-width: 25rem;"
                />
                <template #prepend>
                    <b-input-group-text>
                        <span class="mdi mdi-magnify"></span>
                    </b-input-group-text>
                </template>
            </b-input-group>
        </b-navbar-nav>
        <b-navbar-nav class="ml-auto">
            <slot></slot>
        </b-navbar-nav>
    </b-nav>
</template>

<script>
export default {
    name: "TheTableCardHeader",
    props: {
        value: {
            type: String | null,
            required: true
        }
    },
}
</script>