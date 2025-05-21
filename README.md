
# Social Website

**Bookmarks** is a Django-based social application designed for users to discover, share, and organize images from the web. It incorporates various features to enhance user interaction and content management.

## Topics Convered

- An authentication system for users to register, log in, edit their profile, and change or reset their password
- A followers' system to allow users to follow each other
- Functionality to display shared images and implement a bookmarklet for users to share images from any website
- An activity stream for each user that allows users to see the content uploaded by the people they follow
- Creating many-to-many relationships
- Customizing behavior for forms
- Using jQuery with Django
- Building a jQuery bookmarklet
- Generating image thumbnails using sorl-thumbnail
- Implementing AJAX views and integrating them with jQuery
- Creating custom decorators for views
- Building AJAX pagination
- Creating an activity stream application
- Adding generic relations to models
- Optimizing QuerySets for related objects
- Using signals for denormalizing counts


[![GitHub - Voblet/bookmarking-for-github: Save and Organize your favorite ...](https://tse2.mm.bing.net/th?id=OIP.D4rHfc0324ABAspquKvNKQE8DF\&pid=Api)](https://github.com/Voblet/bookmarking-for-github)

Here’s a concise README summary for the [SulemanMughal/bookmarks](https://github.com/SulemanMughal/bookmarks) repository:


## Technologies Used

* **Backend**: Django
* **Frontend**: jQuery
* **Image Handling**: sorl-thumbnail
* **AJAX**: For dynamic content loading
* **Database**: PostgreSQL (assumed based on Django's default)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/SulemanMughal/bookmarks.git
   cd bookmarks
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Apply migrations:

   ```bash
   python manage.py migrate
   ```

4. Create a superuser to access the admin panel:

   ```bash
   python manage.py createsuperuser
   ```

5. Run the development server:

   ```bash
   python manage.py runserver
   ```

6. Access the application at `http://127.0.0.1:8000/`.

## Contributing

Contributions are welcome! Please fork the repository, make your changes, and submit a pull request.
