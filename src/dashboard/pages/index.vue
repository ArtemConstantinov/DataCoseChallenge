<template>
    <TheTableCard 
        :fields="fields" 
        :items="authors" 
        add-new-label="Add author"
        @on-delete="onDeleteAuthor"
        ref="authorsTable"
    >
        <template #modal="{show, edit, editItem, onClose}">
            <TheAddEditModal
                add-title="Add new author"
                edit-title="Edit author"
                :show="show"
                :edit="edit"
                @hide="() => onClose(false)"
                @on-create-new="onCreateAuthor"
                @on-edit="onEditAuthor"
                @on-delete="onDeleteAuthor"
            >
                <TheAuthorForm 
                    :value="editItem" 
                    @input="updateFormData" 
                    @on-delete-book="onDeleteBook"
                />
            </TheAddEditModal>
        </template>
    </TheTableCard>
</template>

<script>
import * as api from "~/lib/api";
import TheTableCard from "~/components/TheTableCard";
import TheAddEditModal from "~/components/TheAddEditModal";
import TheAuthorForm from "~/components/forms/TheAuthorForm";

export default {
    layout: "default",
    name: "authors-page",
    components: {
        TheTableCard,
        TheAddEditModal,
        TheAuthorForm
    },
    head() {
        return {
            title: "Authors",
            meta: [
                { name: "description", content: "The list of authors." }
            ]
        }
    },
    data() {
        return {
            fields: [
                { key: "name", label: "Name", sortable: false },
                { key: "num_books", label: "Number of books", class: "text-center", sortable: false },
                { key: "actions", label: "Actions", class: "text-right", tdClass: "text-right" }
            ],
            add_edit_form: {}
        }
    },
    computed: {
        authors() { return this.$store.state.authors; },
    },
    async asyncData({ $axios, store }) {
        if (store.state.books.length == 0) {
            const books = await api.getAllBooks($axios);
            store.commit("SET_BOOKS", books);
        }
        const authors = await api.getAllAuthors($axios);
        store.commit("SET_AUTHORS", authors);
    },
    methods: {
        updateFormData(val) {
            this.add_edit_form = val;
        },
        async onCreateAuthor() {
            const payload = {name: this.add_edit_form.name};
            const newAuthor = await api.createAuthor(this.$axios, payload);
            if (!newAuthor) return;
            this.add_edit_form.new_books.forEach(async (book) => { await this.createBook({...book, author_id: newAuthor.id}) });
            const author = await api.getAuthor(this.$axios, newAuthor.id);
            if (!author) return;
            this.$store.dispatch("ACT_ADD_AUTHOR", author);
            this.$refs.authorsTable.completeAction()
        },
        async onEditAuthor() {
            const payload = {name: this.add_edit_form.name};
            const author = await api.editAuthor(this.$axios, this.add_edit_form.id, payload);
            if (!author) return;
            this.add_edit_form.new_books.forEach(async (book) => { await this.createBook({...book, author_id: author.id}) });
            this.add_edit_form.books.forEach(async (book) => { await this.editBook(book) });
            const author_refresh = await api.getAuthor(this.$axios, author.id);
            if (!author_refresh) return;
            this.$store.dispatch("ACT_UPDATE_AUTHOR", author_refresh);
            this.$refs.authorsTable.completeAction()
        },
        async onDeleteAuthor(authorId) {
            const id = authorId || this.add_edit_form.id;
            const deletedAuthorId = await api.deleteAuthor(this.$axios, id);
            if (!deletedAuthorId) return;
            this.$store.dispatch("ACT_DEL_AUTHOR", deletedAuthorId);
            this.$refs.authorsTable.completeAction()
        },
        async createBook(book) {
            const newBook = await api.createBook(this.$axios, book);
            if (!newBook) return;
            this.$store.dispatch("ACT_ADD_BOOK", newBook);
        },
        async editBook(book) {
            const edtBook = await api.editBook(this.$axios, book.id, book);
            if (!edtBook) return;
            this.$store.dispatch("ACT_UPDATE_BOOK", edtBook);
        },
        async onDeleteBook(book) {
            const deletedBookId = await api.deleteBook(this.$axios, book.id);
            if (!deletedBookId) return;
            this.$store.dispatch("ACT_DEL_BOOK", deletedBookId);
            const author_refresh = await api.getAuthor(this.$axios, book.author_id);
            if (!author_refresh) return;
            this.$store.dispatch("ACT_UPDATE_AUTHOR", author_refresh);
        },
    }
}
</script>