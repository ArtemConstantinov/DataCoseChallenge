<template>
    <b-card class="content-card" bg-variant="light" header-tag="nav">
        <template #header>
            <TheTableCardHeader v-model="filter">
                <b-button variant="primary" @click="showModal = !showModal">
                    <span 
                        class="mdi mdi-plus" 
                        style="margin-right: 0.4rem;"
                    ></span>
                    {{ addNewLabel }}
                </b-button>
            </TheTableCardHeader>
        </template>
        
        <b-table 
            sticky-header
            show-empty
            borderless
            hover
            head-variant="light"
            :items="items"
            :fields="fields"
            :current-page="currentPage"
            :per-page="perPage"
            :filter="filter"
            :filter-included-fields="filterOn"
            @filtered="onFiltered"
            class="the-table"
        >
            <template #cell(actions)="row">
                <b-button 
                    size="sm" 
                    @click="onClickEdit(row.item, row.index, $event.target)" 
                    class="mr-1"
                    v-b-tooltip.hover
                    delay="500"
                    title="Edit" 
                >
                    <span class="mdi mdi-file-edit-outline"></span>
                </b-button>
                <b-button 
                    size="sm" 
                    @click="onClickDelete(row.item, $event.target)" 
                    variant="danger"
                    v-b-tooltip.hover
                    delay="500"
                    title="Delete" 
                >
                    <span class="mdi mdi-delete-outline"></span>
                </b-button>
            </template>
        </b-table>
        <div class="pagination-container">
            <b-pagination 
                pills 
                v-model="currentPage"
                :total-rows="totalRows"
                :per-page="perPage"
            />
        </div>

        <slot 
            name="modal"
            :show="showModal"
            :edit="isEditModal" 
            :editItem="itemToEdit"
            :onClose="onModalClose"
        ></slot>
    </b-card>
</template>

<script>

import TheTableCardHeader from "./TheTableCardHeader.vue";

export default {
    props: {
        items: {
            type: Array,
            default: () => []
        },
        fields: {
            type: Array,
            required: true,
        },
        addNewLabel: {
            type: String,
            default: "Add"
        }
    },
    data() {
        return {
            filter: null,
            filterOn: [],
            perPage: 10,
            totalRows: 1,
            currentPage: 1,
            showModal: false,
            isEditModal: false,
            itemToEdit: null,
        }
    },
    watch: {
        items: {
            handler(nv) {
                this.totalRows = nv.length
            },
            immediate: true
        }
    },
    methods: {
        completeAction() {
            this.showModal = false
        },
        onClickEdit(rowItem, rowIndex, target) {
            this.itemToEdit = { ...rowItem };
            this.isEditModal = true;
            this.showModal = !this.showModal;
        },
        onClickDelete(rowItem, target) {
            this.$emit("on-delete", rowItem.id);
        },
        onFiltered(filteredItems) {
            this.totalRows = filteredItems.length
            this.currentPage = 1
        },
        onModalClose(v) {
            this.showModal = v
            setTimeout(() => {
                this.isEditModal = false;
                this.itemToEdit = null;
            }, 500);
            
        }
    }
}
</script>

<style lang="scss" scoped>
.content-card 
{
    width: 100%;
    margin-top: 3rem;
    justify-self: center;
    height: calc(100vh - 15rem);

    .pagination-container 
    {
        display: grid;
        justify-items: end;
    }

    .the-table
    {
        height: 100%;
        max-height: calc(100vh - 24.5rem);
        
    }
}
</style>