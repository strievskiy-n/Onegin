<!DOCTYPE html>

<html>
<head>
<link rel="shortcut icon" href="http://images.easyfreeclipart.com/288/book-clipart-cliparts-of-free-download-wmf-eps-emf-svg-png--288983.png" type="image/png">
<title>Евгений Онегин: поиск</title>

</link>
<link href=’http://fonts.googleapis.com/css?family=Jura&subset=cyrillic,latin’ rel=’stylesheet’ type=’text/css’></link>

<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.5.0/css/font-awesome.min.css"/>
<link rel="stylesheet" href="css/style.css"/>


</head>
<body>



<h2> Евгений Онегин: поиск </h2>
<div class="post-detail">
    <span class="post-info">
        <span>Александр Сергеевич Пушкин</span>
    </span>
</div>
<p>               </p>


<p class="center-img">
<img src="img/picture1.jpg" width="600"  class="center-img"> 
</p>
<form action="" method="get">
  <input name="s" placeholder="Искать здесь..." type="search" value="{{query}}">
  <button type="submit"></button>
</form>




% for r in data:
  <p>               </p>
  <div class="post-header">
    <div class="post-cat">
      <a href="#">{{r[1][1]}}</a>
    </div>
    <div class="post-title">
      <p>
        <a href="#">
          %for string in r[0].split('\n'):
            {{string}}
            <br>
          %end
        </a>
      </p>
    </div>
    <div class="post-meta"><a href="#"></a> </div>
    <div class="border">
      <span></span>
      <span></span>
      </div>
   </div>
 %end


 </body>
</html>