from flask import Flask, render_template, request, redirect, session
from library import Library
from admin import Admin
import random
import string
import os
from dotenv import load_dotenv

app = Flask(__name__)

# Used by Flask to securely sign session data.
# In a real production app, this should be a long random secret
# stored in an environment variable instead of being written here.
load_dotenv()
app.secret_key = os.getenv("SECRET_KEY")

library = Library()
library.load_data()

# Simple admin account for the application.
admin = Admin("admin", "1234")


@app.route("/")
def home():
    return render_template("index.html")


# =========================
# MEMBER
# =========================

@app.route("/member/register", methods=["POST"])
def register_member():

    name = request.form["name"].strip().title()

    # Generate a unique 5-digit member ID.
    while True:

        member_id = str(random.randint(10000, 99999))

        if member_id not in library.members:
            break

    member = library.register_member(name, member_id)

    library.save_data()

    # Store the member ID in the session so the member
    # remains logged in while navigating the application.
    session["member_id"] = member.member_id

    return redirect("/member")


@app.route("/member/login", methods=["POST"])
def member_login():

    member_id = request.form["member_id"].strip()

    member = library.find_member(member_id)

    if member:
        session["member_id"] = member.member_id
        return redirect("/member")

    return render_template(
        "index.html",
        member_error="Invalid Member ID. Please check your ID and try again."
    )


@app.route("/member")
def member_dashboard():

    # Retrieve the logged-in member's ID from the session.
    member_id = session.get("member_id")

    if not member_id:
        return redirect("/")

    member = library.find_member(member_id)

    if not member:
        return redirect("/")

    books = library.get_all_books()

    return render_template(
        "member.html",
        member=member,
        books=books
    )


@app.route("/borrow/<isbn>", methods=["POST"])
def borrow_book(isbn):

    member_id = session.get("member_id")

    member = library.find_member(member_id)

    success, book = library.find_book(isbn)

    if member and success:

        member.borrow_book(book)

        # Save the updated borrowing information to the JSON file.
        library.save_data()

    return redirect("/member")


@app.route("/return/<isbn>", methods=["POST"])
def return_book(isbn):

    member_id = session.get("member_id")

    member = library.find_member(member_id)

    success, book = library.find_book(isbn)

    if member and success:

        member.return_book(book)

        # Save the updated borrowing information to the JSON file.
        library.save_data()

    return redirect("/member")


# =========================
# ADMIN
# =========================

@app.route("/admin/login", methods=["POST"])
def admin_login():

    username = request.form["username"].strip()
    password = request.form["password"].strip()

    if admin.authenticate(username, password):

        # Store a simple flag indicating that the admin is authenticated.
        session["admin"] = True

        return redirect("/admin")

    return render_template(
        "index.html",
        admin_error="Invalid admin username or password."
    )


@app.route("/admin")
def admin_dashboard():

    # Prevent users who are not logged in as admin
    # from accessing the admin dashboard.
    if not session.get("admin"):
        return redirect("/")

    books = library.get_all_books()
    members = library.get_members()

    return render_template(
        "admin.html",
        books=books,
        members=members
    )


@app.route("/admin/add-book", methods=["POST"])
def add_book():

    if not session.get("admin"):
        return redirect("/")

    title = request.form["title"].strip().title()
    author = request.form["author"].strip().title()

    # Generate a unique 5-character ISBN-like identifier.
    while True:

        isbn = "".join(
            random.choices(
                string.ascii_letters + string.digits,
                k=5
            )
        )

        if isbn not in library.books:
            break

    library.add_book(title, author, isbn)

    library.save_data()

    return redirect("/admin")


@app.route("/admin/delete/<isbn>", methods=["POST"])
def delete_book(isbn):

    if not session.get("admin"):
        return redirect("/")

    library.remove_book(isbn)

    library.save_data()

    return redirect("/admin")


@app.route("/logout")
def logout():

    # Remove all stored session data, logging the current user out.
    session.clear()

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)