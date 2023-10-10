// Books

export async function createBook(axios, book) {
    try {
        const response = await axios.post("/books", book);
        return response.data;
    } catch (err) {
        console.error(err);
        return null;
    }

};

export async function getAllBooks(axios) {
    try {
        const response = await axios.get("/books");
        return response.data.books
    } catch (err) {
        console.error(err);
        return []
    }
};

export async function getBook(axios, bookId) {
    try {
        const response = await axios.get(`/books/${bookId}`);
        return response.data;
    } catch (err) {
        console.error(err);
        return null
    }

};

export async function editBook(axios, bookId, book) {
    try {
        const response = await axios.put(`/books/${bookId}`, book);
        return response.data;
    } catch (err) {
        console.error(err);
        return null;
    }

};

export async function deleteBook(axios, bookId) {
    try {
        const response = await axios.delete(`/books/${bookId}`);
        return response.data.book_id;
    } catch (err) {
        console.error(err);
        return null;
    }

};


// Authors

export async function getAllAuthors(axios) {
    try {
        const response = await axios.get("/authors");
        return response.data.authors
    } catch (err) {
        console.error(err);
        return []
    }
};

export async function createAuthor(axios, author) {
    try {
        const response = await axios.post("/authors", author);
        return response.data;
    } catch (err) {
        console.error(err);
        return null;
    }
};

export async function getAuthor(axios, authorId) {
    try {
        const response = await axios.get(`/authors/${authorId}`);
        return response.data;
    } catch (err) {
        console.error(err);
        return null;
    }

};

export async function editAuthor(axios, authorId, author) {
    try {
        const response = await axios.put(`/authors/${authorId}`, author);
        return response.data;
    } catch (err) {
        console.error(err);
        return null;
    }
};

export async function deleteAuthor(axios, authorId) {
    try {
        const response = await axios.delete(`/authors/${authorId}`);
        return response.data.author_id;
    } catch (err) {
        console.error(err);
        return null;
    }
};