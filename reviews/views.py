import imp
from django.shortcuts import render, redirect, get_object_or_404

from common.models import User
from .forms import *
from common.decorators import login_required

# Create your views here.
def index(request):
    return render(request, "index.html")

@login_required
def reviewList(request, **kwargs):
    context = {}
    context['login_session'] = kwargs.get("login_session")

    from django.db.models import Window, F
    from django.db.models.functions import RowNumber
    boards = Board.objects.select_related('writer').filter(category='review').annotate(row_number=Window(expression=RowNumber(), order_by=F('bno').asc())).order_by("-bno")

    context['boards'] = boards
    
    return render(request, "review_list.html", context)


@login_required
def writeReview(request, **kwargs):
    context = {}
    context['login_session'] = kwargs.get("login_session")

    if request.method == 'GET':
        review_form = ReviewWriteForm()
        context['forms'] = review_form
        return render(request, "review_write.html", context)

    elif request.method == 'POST':
        review_form = ReviewWriteForm(request.POST)

        if review_form.is_valid():
            login_session = request.session.get('user', '')
            writer = User.objects.get(id=login_session)
            meta_json = {'scope': review_form.meta_json}

            board = Board(
                title=review_form.title,
                contents=review_form.contents,
                writer=writer,
                category='review',
                meta_json=str(meta_json)
            )
            board.save()
            return redirect('/review')
        else:
            '''
            context['forms'] = join_form
            if join_form.errors:
                for value in join_form.errors.values():
                    context['error'] = value
            '''
            context['forms'] = review_form
        return render(request, "review_write.html", context)


def reviewDetail(request, pk):
    context = {}
    login_session = request.session.get("user", "")
    context['login_session'] = login_session
    board = get_object_or_404(Board.objects.select_related('writer'), bno=pk)
    json_scope = board.meta_json

    board.hits += 1
    board.save()

    from ast import literal_eval
    scope = literal_eval(json_scope)
    
    scope_form = ScopeForm(value=scope["scope"])

    context['board'] = board
    context['scope'] = scope_form

    if board.writer.id == login_session:
        context['writer'] = True
    else:
        context['writer'] = False

    return render(request, "review_detail.html", context)


def reviewModify(request, pk):
    login_session = request.session.get("user", "")

    context = {}
    context['login_session'] = login_session

    board = get_object_or_404(Board, bno=pk)
    context['board'] = board

    if board.writer.id != login_session:
        return redirect(f'/review/detail/{pk}/')

    if request.method == 'GET':
        review_form = ReviewWriteForm(instance=board)
        context['forms'] = review_form
        return render(request, "review_modify.html", context)

    elif request.method == 'POST':
        review_form = ReviewWriteForm(request.POST)

        if review_form.is_valid():
            login_session = request.session.get('user', '')
            writer = User.objects.get(id=login_session)
            meta_json = {'scope': review_form.meta_json}

            board.title = review_form.title
            board.contents = review_form.contents
            board.meta_json = str(meta_json)
            
            board.save()
            return redirect('/review')
        else:
            '''
            context['forms'] = join_form
            if join_form.errors:
                for value in join_form.errors.values():
                    context['error'] = value
            '''
            context['forms'] = review_form
        return render(request, "review_modify.html", context)


def reviewDelete(request, pk):
    login_session = request.session.get("user", "")

    board = get_object_or_404(Board, bno=pk)
    
    if board.writer.id == login_session:
        board.delete()
        return redirect('/review')
    else:
        return redirect(f'/review/detail/{pk}/')

