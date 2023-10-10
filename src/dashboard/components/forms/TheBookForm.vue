<template>  
    <b-form>
        <b-form-group 
            v-for="(field, idx) in schema"
            :key="idx"
            :id="`input-group-${idx}`" 
            :label="field.label" 
            :label-for="`input-${idx}`"
        >
            <component
                :is="field.componentName"
                :value="form[field.fieldName]"
                @input="updateForm(field.fieldName, $event)"
                v-bind="field.props"
            />
        </b-form-group>
    </b-form>
</template>

<script>
 // import the component
import Treeselect from "@riophae/vue-treeselect";
  // import the styles
import "@riophae/vue-treeselect/dist/vue-treeselect.css";

export default {
    name: "ThBookForm",
    components: {
        Treeselect
    },
    props: {
        value: {
            type: Object | null,
            default: null
        }
    },
    data() {
        return {
            form: this.value || {
                title: "",
                pages: 0,
                author_id: null
            },
        }
    },
    watch: {
        value: {
            handler(nv, ov) {
                if (nv && nv !== ov) {
                    this.form = nv
                }
            },
            deep: true
        }
    },
    mounted() {
        this.$emit("input", this.form);
    },
    methods: {
        updateForm(fieldName, value) {
            this.$set(this.form, fieldName, value);
            this.$emit("input", this.form);
        }
    },
    computed: {
        options() {
            return this.$store.state.authors.map(({id, name}) => ({id, label: name}))
        },
        schema() {
            return [
                {
                    label: "Book title:",
                    componentName: "b-form-input",
                    fieldName: "title",
                    props: {
                        placeholder: "Enter title",
                        required: true
                    }
                },
                {
                    label: "Pages number:",
                    componentName: "b-form-input",
                    fieldName: "pages",
                    props: {
                        id: null,
                        placeholder: "Enter pages count",
                        type: "number",
                        required: true
                    }
                },
                {
                    label: "Books author:",
                    componentName: "Treeselect",
                    fieldName: "author_id",
                    props: {
                        placeholder: "Select author",
                        required: true,
                        multiple: false,
                        options: this.options
                    }
                },
            ]
        }
    },

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