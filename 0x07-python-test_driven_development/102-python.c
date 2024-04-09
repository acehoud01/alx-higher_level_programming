#include <Python.h>
#include <stdio.h>

/**
 * print_python_string - Prints Python strings.
 *
 * @@p: PyObject pointer to the Python string.
 * Return: nothing
 */

void print_python_string(PyObject *p)
{
	if (!PyUnicode_Check(p))
	{
		fprintf(stderr, "[ERROR] Invalid Python string\n");
		return;
	}

	Py_ssize_t size;
	const char *str = PyUnicode_AsUTF8AndSize(p, &size);

	if (!str)
	{
		fprintf(stderr, "[ERROR] Unable to convert Python string to UTF-8\n");
		return;
	}
	printf("String: \"%s\"\n", str);
	printf("Length: %ld\n", (long)size);
}
