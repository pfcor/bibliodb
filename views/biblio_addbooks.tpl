<!DOCTYPE html>

<html>
  <head>
    <title>biblioDB</title>

    <style type="text/css">
      .label {text-align: right}
      .error {color: red}
    </style>

  </head>

  <body>
    Let's add a new book!<br>
    <h2>Book data:</h2>
    <form method="post">
      <table>
        <tr>
          <td class="label">
            Title
          </td>
          <td>
            <input type="text" name="title" value="">
          </td>
        </tr>

        <tr>
          <td class="label">
            Author
          </td>
          <td>
            <input type="text" name="author" value="">
          </td>
        </tr>

        <tr>
          <td class="label">
            Year
          </td>
          <td>
            <input type="text" name="year" value="">
          </td>
        </tr>

      </table>

      <input type="submit">
    </form>
  </body>

</html>
