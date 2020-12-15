%{
#include "kiva_rect.h"
%}

%typemap(in)  (kiva::rect_type &rect) 
{   
    PyArrayObject* ary=NULL;
    int is_new_object; 
    ary = obj_to_array_contiguous_allow_conversion($input, PyArray_DOUBLE,
                                                   is_new_object);

    int size[1] = {4};
    if (!ary || 
        !require_dimensions(ary, 1) ||
        !require_size(ary, size, 1))
    {    
        goto fail;
    }

    double* data = (double*)(ary->data);
    kiva::rect_type rect(data[0], data[1], 
                         data[2], data[3]);
    $1 = &rect;
    
    if (is_new_object)
    {
        Py_DECREF(ary);
    }
}

%typemap(out) kiva::rect_type
{
    PyObject *pt = PyTuple_New(4);
    PyTuple_SetItem(pt,0,PyFloat_FromDouble($1.x));
    PyTuple_SetItem(pt,1,PyFloat_FromDouble($1.y));
    PyTuple_SetItem(pt,2,PyFloat_FromDouble($1.w));
    PyTuple_SetItem(pt,3,PyFloat_FromDouble($1.h));
    $result = pt;
}
