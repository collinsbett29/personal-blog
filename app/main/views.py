from flask import render_template,request,url_for
from . import main
from .forms import PostForm,BlogForm
from.. import db

@main.route('/')
def index():
    '''
    view root that returns the index page and its data
    '''
    blog = Blog.get_blogs()

    return render_template('index.html' blog = blog)

@main.route('add/blog', methods=['GET','POST'])
def new_blog():
    '''
    view new route that returns a page with a form to create a new blog
    '''
    form = BlogForm()

    if form.validate_on_submit():
        name = form.name.data
        new_blog = Blog(name=name)
        new_blog.save_blog()

        return redirect(url_for('.index')) 

    title = 'New blog' 
    return render_template('new_blog.html', BlogForm = form,title = title)
@main.route('/blogs/<int:id>')
def blog(id):
    blog = Blog.query.get(id)    
    posts = Post.query.filter_by(blog=blog_.id).all

    return render_template('blog.html', posts=posts, blog=blog_)

@main.route('/blogs/view_post/add/<int:id>', methods=['GET','POST'])
def new_post(id):
    '''
    function to check posts form and fetch data from the fields
    '''
    form = PostForm()
    blog =Blog.query.filter_by(id=id).first()

    if blog is None:
        abort(404)

    if form.validate_on_submit():
        content = form.content.data
        new_post = POst(content=content,blog=blog.id,user_id=current_user.id)   
        new_post.save_post()
        return redirect(url_for('.blog',id=blog.id)) 

    title = 'New Post'
    return render_template('new_post.html', title = title, post_form = form, blog = blog)

@main.route('/blogs/view_post/<int:id>', methods =['GET', 'POST'])
def view_post(id):
    '''
    function that returns a single post for comment to be added
    '''

    print(id)
    posts = Post.query.get(id)

    if posts is None:
        abort(404)

    comment = Comments.get_comments(id)
    return render_template('post.html', posts = posts, comment=comment, blog_id=id)
        



