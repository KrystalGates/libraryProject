import sqlite3
from django.shortcuts import render
from libraryapp.models import Library
from libraryapp.models import model_factory
from ..connection import Connection
from django.contrib.auth.decorators import login_required

@login_required
def list_libraries(request):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = model_factory(Library)
        db_cursor = conn.cursor()

        db_cursor.execute("""
        select
            id,
            title,
            address
        from libraryapp_library
        """)

        all_libraries = db_cursor.fetchall()

    template_name = 'libraries/list.html'
    return render(request, template_name, {'all_libraries': all_libraries})