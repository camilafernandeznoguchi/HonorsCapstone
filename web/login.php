<?php
   session_start();
   
   error_reporting(0);
   mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);
   
   try {
        if($_SERVER["REQUEST_METHOD"] == "POST") {
            // username and password sent from form 

            $myusername = $_POST['username'];
            $mypassword = $_POST['password'];

            //connect to db
            include("config.php");
            if (mysqli_connect_error($db)) {
                echo "Failed to connect to MySQL: " . mysqli_connect_error() . "<br>";
                exit("Connect Error");
            }

            // test for HTML characters to avoid HTML Injection
            require ("testInput.php");
            $myusername = test_input($myusername);
            $mypassword = test_input($mypassword);

            //prepare SQL query to validate email
            $query = mysqli_prepare($db, "SELECT * FROM user WHERE username=? AND userPassword =MD5(?)");
            mysqli_stmt_bind_param($query, "ss", $myusername, $mypassword);
            mysqli_stmt_execute($query);
            $result = mysqli_stmt_get_result($query);

            // if more than 1 person with same email, redirect to error page and try again
            $rows = mysqli_num_rows($result);

            if($rows == 1) {
                #session_register("myusername");
                $_SESSION['login_user'] = $myusername;
                header("location: index.php");
            }else {
                $error = "Your Login Name or Password is invalid";
                echo $error;
            }
        }
   } catch (Exception $e) {
        $error_message = $e->getMessage() . "<br>Line" . $e->getLine();
        echo $error_message;
  } finally {
        // close connection
        mysqli_close($db);
  }
?>

<!DOCTYPE html>
<html lang="en">

<head>
  <!-- Required meta tags -->
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <title>Smart Composting Collection Bin-Login</title>
  <!-- plugins:css -->
  <link rel="stylesheet" href="vendors/feather/feather.css">
  <link rel="stylesheet" href="vendors/mdi/css/materialdesignicons.min.css">
  <link rel="stylesheet" href="vendors/ti-icons/css/themify-icons.css">
  <link rel="stylesheet" href="vendors/typicons/typicons.css">
  <link rel="stylesheet" href="vendors/simple-line-icons/css/simple-line-icons.css">
  <link rel="stylesheet" href="vendors/css/vendor.bundle.base.css">
  <!-- endinject -->
  <!-- Plugin css for this page -->
  <!-- End plugin css for this page -->
  <!-- inject:css -->
  <link rel="stylesheet" href="css/vertical-layout-light/style.css">
  <!-- endinject -->
  <link rel="shortcut icon" href="images/favicon.png" />
</head>

<body>
  <div class="container-scroller">
    <div class="container-fluid page-body-wrapper full-page-wrapper">
      <div class="content-wrapper d-flex align-items-center auth px-0">
        <div class="row w-100 mx-0">
          <div class="col-lg-4 mx-auto">
            <div class="auth-form-light text-left py-5 px-4 px-sm-5">
              <div class="brand-logo">
              	<h4 style="font-weight: bolder;">Smart Composting <span style="color: #233eac">Collection Bin</span></h4>
              </div>
              <h4>Hello! let's get started</h4>
              <h6 class="fw-light">Sign in to continue.</h6>
              <form class="pt-3" action="" method="post">
                <div class="form-group">
                  <input type="text" class="form-control form-control-lg" id="exampleInputEmail1" placeholder="Username" name="username">
                </div>
                <div class="form-group">
                  <input type="password" class="form-control form-control-lg" id="exampleInputPassword1" placeholder="Password" name = "password">
                </div>
                <div class="mt-3">
                  <input type="submit" value="SIGN IN" class="btn btn-block btn-primary btn-lg font-weight-medium auth-form-btn"/>
                </div>
                <!-- 
                <div class="text-center mt-4 fw-light">
                  Don't have an account? <a href="register.html" class="text-primary">Create</a>
                </div>
                -->
              </form>
            </div>
          </div>
        </div>
      </div>
      <!-- content-wrapper ends -->
    </div>
    <!-- page-body-wrapper ends -->
  </div>
  <!-- container-scroller -->
  <!-- plugins:js -->
  <script src="vendors/js/vendor.bundle.base.js"></script>
  <!-- endinject -->
  <!-- Plugin js for this page -->
  <script src="vendors/bootstrap-datepicker/bootstrap-datepicker.min.js"></script>
  <!-- End plugin js for this page -->
  <!-- inject:js -->
  <script src="js/off-canvas.js"></script>
  <script src="js/hoverable-collapse.js"></script>
  <script src="js/template.js"></script>
  <script src="js/settings.js"></script>
  <script src="js/todolist.js"></script>
  <!-- endinject -->
</body>

</html>
