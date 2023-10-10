<template> 
    <b-form>
        <b-form-group id="input-group-1" label="Author name:" label-for="input-1">
            <b-form-input
                id="input-1"
                :value="form.name"
                @input="updateForm('name', $event)"
                placeholder="Enter author name"
                required
            />
        </b-form-group>

        <TheFormActionBar @on-add="onAddNew"/>

        <TheBooksEditableTable 
            :items="books"
            :fields="fields"
            :getFieldMethod="getBookField"
            @on-field-input="updateBookField"
            @row-clicked="onRowClick"
            @on-delete="onClickDelete"
        />
    </b-form>
</template>

<script>
import { v4 as uuidv4 } from "uuid";
import TheFormActionBar from "./TheFormActionBar";
import TheBooksEditableTable from "./TheBooksEditableTable";

export default {
    name: "ThAuthorsForm",
    components: {
        TheFormActionBar,
        TheBooksEditableTable
    },
    props: {
        value: {
            type: Object | null,
            default: null
        }
    },
    data() {
        return {
            form: {...this.value, books: [], new_books: []} || {
                id: null,
                name: "",
                books: [],
                new_books: []
            },
            fields: [
                { key: "selected" },
                { key: "title", label: "Title", sortable: false, colon: 2 },
                { key: "pages", label: "№ Pages", sortable: false, class: "text-left" },
                { key: "actions", label: "Actions", class: "text-center" }
            ],
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
        this.$emit("input", this.cleanupData(this.form));
    },
    computed: {
        books() {
            const authorBooks = this.$store.getters.getBooksByAuthorId(this.value?.id);
            const allBooks = [...this.form.new_books, ...authorBooks];
            return allBooks.map((book) => {
                return {
                    ...book,
                    isSelected: this.selectedIds.includes(book.id) || book.isNew,
                }
            });
        },
        selectedIds() {
            return this.form.books.map((b) => b.id);
        }
    },
    methods: {
        onAddNew() {
            const newBook = {
                isNew: true,
                id: uuidv4(),
                title: "", 
                pages: 0, 
                author_id: this.value?.id || null
            };
            this.$set(this.form, "new_books", [...this.form.new_books, newBook]);
        },
        onClickDelete(item) {
            if (item.isNew) {
                const new_books = this.form.new_books.filter((b) => b.id !== item.id)
                this.$set(this.form, "new_books", new_books);
                return;
            }
            this.$emit("on-delete-book", item)
        },
        updateForm(fieldName, value) {
            this.$set(this.form, fieldName, value);
            this.$emit("input", this.cleanupData(this.form));
        },
        cleanupData(form) {
            return {
                id: form.id,
                name: form.name,
                new_books: form.new_books.map(({title, pages, author_id}) => ({title, pages, author_id})),
                books: form.books.map(({id, title, pages, author_id}) => ({id, title, pages, author_id}))
            }
        },
        onRowClick(item, index, event) {
            if (item.isNew) return;
            if (!item.isSelected)
                return this.updateForm("books", [...this.form.books, item]); // Append book
            // Remove book
            const books = this.form.books.filter((book) => book.id !== item.id);
            return this.updateForm("books", books);
        },
        getBookField(id, key, isNew) {
            let book = isNew? 
                    this.form.new_books.find((b) => b.id === id):
                    this.form.books.find((b) => b.id === id);
            return book[key]
        },
        updateBookField({id, key, value}) {
            let collection = this.form.books;
            let collection_key = "books";
            if (!this.selectedIds.includes(id)) {
                collection = this.form.new_books;
                collection_key = "new_books";
            }
            const books = collection.map(
                (book) => {
                    if (book.id === id) {
                        const new_book = {...book}
                        new_book[key] = value
                        return new_book
                    }
                    return book
                }
            )
            this.updateForm(collection_key, books)
        }
    },
}
</script>