$(function () {
    $('#b04').unslider({
        dots: true
    });

    $("#cate_id>li").mouseover(function () {
        $('.sub').hide();
        $(this).find('ul').show()
    });

    $("#cate_id").mouseleave(function () {
        $(this).find('ul').hide()
    });
});

