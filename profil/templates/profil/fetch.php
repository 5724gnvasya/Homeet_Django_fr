<?php
    $name = $_Get['name'];

    $fp = fopen("data.txt", "name");//open file in writing mode
    $mytext = "$name User's data\r\n"; //исходная строка
    $test = fwrite($fp, $mytext);
    if ($test) echo 'Данные в файл успешно занесены.';
    else echo 'Ошибка при записи в файл.';
    fclose($fp);// closing the file

?>

