function showPanel(panelId) {

    const memberPanel =
        document.getElementById("memberPanel");

    const adminPanel =
        document.getElementById("adminPanel");

    const tabs =
        document.querySelectorAll(".tab");


    memberPanel.classList.add("hidden");
    adminPanel.classList.add("hidden");


    document.getElementById(panelId)
        .classList.remove("hidden");


    tabs.forEach(function(tab) {
        tab.classList.remove("active");
    });


    if (panelId === "memberPanel") {
        tabs[0].classList.add("active");
    } else {
        tabs[1].classList.add("active");
    }
}


/* =========================
   MEMBER BOOK SEARCH
========================= */

const bookSearch =
    document.getElementById("bookSearch");


if (bookSearch) {

    const books =
        document.querySelectorAll(".book-card");


    bookSearch.addEventListener("input", function() {

        const keyword =
            bookSearch.value.toLowerCase();


        books.forEach(function(book) {

            const text =
                book.dataset.search.toLowerCase();


            if (text.includes(keyword)) {

                book.style.display = "grid";

            } else {

                book.style.display = "none";

            }

        });

    });

}


/* =========================
   ADMIN BOOK SEARCH
========================= */

const adminSearch =
    document.getElementById("adminBookSearch");


if (adminSearch) {

    const books =
        document.querySelectorAll(".admin-book");


    adminSearch.addEventListener("input", function() {

        const keyword =
            adminSearch.value.toLowerCase();


        books.forEach(function(book) {

            const text =
                book.dataset.search.toLowerCase();


            if (text.includes(keyword)) {

                book.style.display = "grid";

            } else {

                book.style.display = "none";

            }

        });

    });

}