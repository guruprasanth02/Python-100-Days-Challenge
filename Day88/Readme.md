# 🌟 Day 88: Customizing User Access and Admin Features in Blog Engine 📝🔐

### 🎊 Today’s Highlights:

* **User Experience Enhancement:** Built a system that allows anyone to read the blog but redirects authenticated users differently based on their identity.

* **Admin Privileges:** Created an admin page that only authorized users (like yourself) can access, while others are told off for trying to access restricted areas.

* **Personalized Responses:** Used the Replit Authentication to check the logged-in user and dynamically change the page content, adding a bit of fun to the user experience.
### 🔍 Key Concepts:

* **Custom Login Flow:** Instead of forcing login at every turn, the blog is publicly accessible, and only those who authenticate are shown specific pages (admin or restricted content).

* **Conditional Redirects:** Used Flask’s ability to check the authenticated user’s username and dynamically decide which page to show (admin access for the right user, and a polite “stop being naughty” message for everyone else).

* **User Identification:** Leveraged Replit's authentication headers (like ```X-Replit-User-Name```) to determine the logged-in user and personalize the experience.

### 👉 Day 88 Challenge:

Enhance your blog engine system by implementing a conditional login flow:

1. Allow everyone to view the blog without logging in.
2. If an authenticated user logs in and it’s you (the admin), redirect them to the admin page.
3. For everyone else, send a polite message telling them they can’t access the admin page.

### 🛠️ Common Errors Encountered:

* **Missing Authentication:** If the user isn’t properly authenticated, they won’t have the necessary headers in the request. Ensure that the Replit Authentication is correctly enabled.

* **Incorrect Username Check:** Always verify that you are using the correct username in the admin check (case-sensitive and exact).


