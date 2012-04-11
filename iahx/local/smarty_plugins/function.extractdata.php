<?php
/**
 * Smarty plugin
 * @package Smarty
 * @subpackage plugins
 */


/**
 * Smarty {extractdata} function plugin
 *
 * Type:     function<br>
 * Name:     occ<br>
 * Date:     Feb 17, 2003<br>
 * Purpose:  return a <br>
 * Input:<br>
 *         - label
 *         - element
 *         - separator
 *         - class
 *
 * Examples:
 * <pre>
 * {occ label=AUTOR element=$doc->au separator=; class=author}
 * </pre>
 * @author   Vinicius Andrade <viniciusdeandrade at gmail dot com>
 * @version  0.1
 * @param array
 * @param Smarty
 * @return string
 */
function smarty_function_extractdata($params, &$smarty)
{
	$output = "";
    $element = $params['element'];
    $part = $params['part'];
    $default = ($params['default'] ? $params['default'] : 'en');
    $separator = ($params['separator'] ? $params['separator'] : '|');
    $data = array();

    if (!isset($element) || $element == '') {
        return;
    }

	if ($part == 'pt')
		$part = 'pt-br';
		
	$current_values = preg_split("/\|/", $element);
	foreach ($current_values as $value){
		$parts = preg_split("/\^/", $value);
		$data[$parts[0]] = $parts[1]; 				
	}
	
	if ($part != ''){
		if ($data[$part] != ''){
			$output = $data[$part];
		}else{
			$output = $data[$default];
		}
	}else{
		$output = $data[$default];
	}	
		
	
    return $output;
}


?>
