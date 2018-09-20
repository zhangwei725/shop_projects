$(function () {
    let delete_url = '/car/delete/';
    let update_url = '/car/update/';
    //通过id获取的选择如果有多个只会选择第一个
    $('.car_btn').click(function () {
        let $btn = $(this);
        $.post(delete_url, {car_id: $(this).attr('car_id')}, function (result) {
            //    当数据库删除了数据  删除该条数据
            if (result.status === 200) {
                //  第一种通过父容器删除子元素
                // 自身删除
                $btn.parents('tr').remove()
            }
        })
    });
    // 商品数量 +
    // 商品数量 -
    $('.add').click(function () {
        //先找td 通过input
        // alert($(this).parent().find(':input[type=text]').val())
        let $input = $(this).next('input');
        let value = parseInt($input.val()) < parseInt($input.attr('max'))
            ? parseInt($input.val()) + 1
            : parseInt($input.attr('max'));
        if (parseInt($input.val()) < parseInt($input.attr('max'))) {
            $.post(update_url, {ac: '1', 'car_id': 12}, function (result) {
                if (result.status === 200) {
                    $input.val(value)
                }
            })
        }

    });
    $('.delete').click(function () {
        // alert($(this).parent().find(':input[type=text]').val())
        let $input = $(this).prev('input');
        let value = $input.val() > 1
            ? $input.val() - 1
            : 1;
        $.post(update_url, {ac: '2', 'car_id': 12}, function (result) {
            if (result.status === 200) {
                $input.val(value)
            }
        })

    })

});