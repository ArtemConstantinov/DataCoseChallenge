<template>
    <TheTableCard 
        :fields="fields" 
        :items="items" 
        add-new-label="Add book"
        @on-delete="onDeleteBook"
    >
        <template #modal="{show, edit, editItem, onClose}">
            <TheAddEditModal
                add-title="Add new book"
                edit-title="Edit book" 
                :show="show"
                :edit="edit"
                @hide="() => onClose(false)"
                @on-create-new="onCreateBook"
                @on-edit="onEditBook"
                @on-delete="onDeleteBook"
            >
                <TheBookForm :value="editItem" @input="updateFormData"/>
            </TheAddEditModal>
        </template>
    </TheTableCard>
</template>

<script>
import * as api from "~/lib/api";
import TheTableCard from "~/components/TheTableCard.vue";
import TheAddEditModal from "~/components/TheAddEditModal";
import TheBookForm from "~/components/forms/TheBookForm.vue";

export default {
    layout: "default",
    name: "books-page",
    components: {
        TheTableCard,
        TheAddEditModal,
        TheBookForm,
    },
    head() {
        return {
            title: "Books",
            meta: [
                { name: "description", content: "The collection of books." }
            ]
        };
    },
    data() {
        return {
            fields: [
                { key: "title", label: "Title", sortable: true },
                { key: "author_name", label: "Author name", sortable: false },
                { key: "pages", label: "Number of pages", class: "text-center", sortable: false },
                { key: "actions", label: "Actions", class: "text-right", tdClass: "text-right" }
            ],
            add_edit_form: {}
        };
    },
    computed: {
        items() {
            return this.$store.getters.getBooks;
        }
    },
    async asyncData({ params, $axios, error, store }) {
        if (store.state.authors.length == 0) {
            const authors = await api.getAllAuthors($axios);
            store.commit("SET_AUTHORS", authors);
        }
        const books = await api.getAllBooks($axios);
        store.commit("SET_BOOKS", books);
    },
    methods: {
        updateFormData(val) {
            this.add_edit_form = val;
        },
        async onCreateBook() {
            const newBook = await api.createBook(this.$axios, this.add_edit_form);
            if (!newBook) return;
            this.$store.dispatch("ACT_ADD_BOOK", newBook);
        },
        async onEditBook() {
            const book = await api.editBook(this.$axios, this.add_edit_form.id, this.add_edit_form);
            if (!book) return;
            this.$store.dispatch("ACT_UPDATE_BOOK", book);
        },
        async onDeleteBook(bookId) {
            const id = bookId || this.add_edit_form.id;
            const deletedBookId = await api.deleteBook(this.$axios, id);
            if (!deletedBookId) return;
            this.$store.dispatch("ACT_DEL_BOOK", deletedBookId);
        },
    }
}

</script>