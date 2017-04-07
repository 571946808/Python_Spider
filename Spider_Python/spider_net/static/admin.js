/**
 * Created by Administrator on 2017/3/23.
 */
$(function(){
    //返回顶部
    $(".backtop").click(function(){
        $("html,body").animate({scrollTop: '0px'}, 1000);
        return false;
    });
    //添加点评
    $(".add").click(function(){
        $(".edit").slideDown('slow');
    });
    //删除点评
    $(".del").click(function(){
        $("form").submit();
    });
    //取消按钮
    $(".list").on('click', '.cancel' ,function(){
        $(".edit").slideUp('slow');
        $("input").val("");
        $("textarea").val("");
    });
});
