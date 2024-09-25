<?php
$taint = some_func($arg1,$arg2, $_GET['tainted']);

if ( isset($_REQUEST['attachment_id']) && ($id = intval($_REQUEST['attachment_id'])) && $_REQUEST['fetch'] ) {
    $post = get_post( $id );
    if ( 'attachment' != $post->post_type )
        wp_die( __( 'Unknown post type.' ) );
    if ( ! current_user_can( 'edit_post', $id ) )
        wp_die( __( 'You are not allowed to edit this item.' ) );

    switch ( $_REQUEST['fetch'] ) {
        case 3 :
            // Title shouldn't ever be empty, but use filename just in case.
            $file = get_attached_file( $post->ID );
            $title = $post->post_title ? $post->post_title : wp_basename( $file );
            // ok: taint-unsafe-echo-tag
            echo '<div class="filename new"><span class="title">' . esc_html( wp_html_excerpt( $title, 60, '&hellip;' ) ) . '</span></div>';
            break;
        }
}

?>
<form>
// ruleid: taint-unsafe-echo-tag
<input type="hidden" name="some_field" value="<?=$taint?>" />
// ok: taint-unsafe-echo-tag
<input type="hidden" name="some_field" value="<?=htmlentities($taint)?>" />
<input type="hidden" name="height" id="height" value="<?php echo esc_attr( $taint ); ?>"/>
</form>

