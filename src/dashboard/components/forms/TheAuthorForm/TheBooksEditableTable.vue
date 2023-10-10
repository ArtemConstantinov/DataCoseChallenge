<template>
    <b-table 
        v-bind="{...table_config.props, ...table_config.bindings}"
        v-on="table_config.events"
    >   
        <template #cell(selected)="{ item }">
            <b-form-checkbox 
                :checked="item.isSelected"
                :disabled="true"
            ></b-form-checkbox>
        </template>

        <template #cell(title)="{ item }">
            <template v-if="item.isSelected || item.isNew">
                <b-form-input 
                    size="sm" 
                    placeholder="Enter book title" 
                    :value="getFieldMethod(item.id, 'title', item.isNew)"
                    @input="onFieldInput(item.id, 'title', $event)"
                    style="max-width: 225px;"
                />
            </template>
            <template v-else>
                {{item.title}}
            </template>
        </template>

        <template #cell(pages)="{ item, field }">
            <template v-if="item.isSelected || item.isNew">
                <b-form-input 
                    size="sm" 
                    placeholder="Enter pages number" 
                    :value="getFieldMethod(item.id, 'pages', item.isNew) || 0"
                    @input="onFieldInput(item.id, 'pages', $event)"
                    style="max-width: 55px;"
                ></b-form-input>
            </template>
            <template v-else>
                {{item.pages}}
            </template>
        </template>

        <template #cell(actions)="{item}">
            <b-button
                size="sm" 
                @click="$emit('on-delete', item)" 
                :variant="item.isNew? 'outline-danger': 'danger'"
                v-b-tooltip.left.hover
                delay="500"
                title="Delete"
                style="margin-right: -12px;"
            >
                <span class="mdi" :class="getRemoveIcon(item)"></span>
            </b-button>
        </template>
    </b-table>

</template>

<script>
export default {
    props: {
        fields: {
            type: Array,
            default: []
        },
        items: {
            type: Array,
            default: []
        },
        getFieldMethod: {
            type: Function,
            required: true,
            default: (id, key, isNew) => null
        },
    },
    computed: {
        table_config() {
            return {
                props: {
                    "sticky-header": true,
                    "show-empty": true,
                    "head-variant": "light",
                    borderless: true,
                    hover: true,
                    small: true,
                    responsive: true,
                    class: "the-table",
                },
                bindings: {
                    "tbody-tr-class": this.rowClass,
                    items: this.items,
                    fields: this.fields,
                },
                events: {
                    "row-clicked": (e) => this.$emit("row-clicked", e)
                }
            }
        },
    },
    methods: {
        getRemoveIcon(item) {
            return (item.isNew)? "mdi-window-close" : "mdi-delete-outline";
        },
        rowClass(item, type) {
            if (!item || type !== "row") return;
            if (item.isNew || item.isSelected) return "table-active";
        },
        onFieldInput(id, key, value) {
            this.$emit("on-field-input", {id, key, value});
        }
    }
}
</script>