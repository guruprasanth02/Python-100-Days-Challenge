# 🌟 Day 79: Form Handling with Flask 🌟

### 🎊 Today’s Highlights:

Today, we dived into handling form submissions on a webpage. We learned how to create an HTML form that collects user input and sends it to the server using the POST method. By adding form fields, buttons, and hidden data, we began building dynamic interactions between a client and server in a web application. The key takeaway: your form doesn't just collect data; it communicates with the backend to process and respond to that data.

### 🔍 Key Concepts:

* **Form Elements:** The ```<form>``` tag is used to wrap inputs, and the ```method``` attribute (usually "post") determines how the data will be sent to the server.
* **Input Fields:** The ```<input>``` tag can be used to collect various types of data, such as text, email, number, and hidden values.
* **Submit Button:** The ```<button>``` tag with ```type="submit"``` sends the form data to the server.
* **Action URL:** The ```action``` attribute in the ```<form>``` tag specifies where the form data should be sent (i.e., to a specific URL or endpoint).

### 👉 Day 79 Challenge: Build a Login Form

**Task Overview:**

Your challenge today is to create a simple login form on a webpage. The form should include fields for:

   * **Username**
   * **Email Address**
   * **Password**

     There should be a **submit** button with the label "login," and the form should submit the data to the /login endpoint using the POST method.

**Example:**
```html
Copy code
<form method="post" action="/login">
  <p>Username: <input type="text" name="username" required></p>
  <p>Email: <input type="email" name="email" required></p>
  <p>Password: <input type="password" name="password" required></p>
  <button type="submit">Login</button>
</form>
```

### 🛠️ Common Errors Encountered:

* **Missing Input ```name``` Attributes:** The ```name``` attribute in form elements is crucial because it defines how data is accessed in the server code. Without it, the data won't be processed properly.

  **Fix:** Always ensure each ```<input>``` tag has a ```name``` attribute.

* **Incorrect Form ```action``` URL:** If the action URL points to a route that doesn't exist or isn't handled properly in your Flask code, the form submission will fail.

  **Fix:** Ensure the ```action``` attribute in the ```<form>``` tag points to the correct server endpoint that processes the data.

* **Missing Submit Button:** Without a submit button, the form won't be submitted, and the user won’t be able to trigger the data submission.

  **Fix:** Always include a button with ```type="submit"``` to trigger the form submission.

### My Code:
```html
<!DOCTYPE html>
<html>

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>replit</title>
  <link href="style.css" rel="stylesheet" type="text/css" />
</head>

<body>

  <form method = "post" action = "/process">
      <p>Username: <input type="text" name="username" required></p>
     <p>Email: <input type="email" name="email" required></p>
     <p>Password: <input type="password" name="password" required></p>
    <button type="submit">Login</button>
  </form>
  <script src="script.js"></script>

  <script src="https://replit.com/public/js/replit-badge.js" theme="blue" defer></script> 
</body>

</html>
