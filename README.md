# Dash Enterprise Dashboard Engine

This directory contains the Limited Availability release of Dash Enterprise Dashboard Engine, which is being made available to select Dash Enterprise customers for evaluation purposes under a time-limited license (see LICENSE file).

If you have any questions or run into any problems with this release of Dashboard Engine, please contact onpremise.support@plot.ly and we will help you out.

Here are the contents of the zip archive:
* `dist/`
  * This directory contains pip-installable tarballs for Dashboard Engine and the latest versions of Dash Design Kit and Dash Snapshot Engine, the three of which are mutually compatible
* `docs/`
  * This directory contains a runnable Dash app which serves as the documentation for Dashboard Engine. 
* `editable_app/`
  * This sample application shows how to use Dashboard Engine in conjunction with Snapshot engine to allow users to “edit the app”. This app is very similar to the “multi dashboard” app except that its root URL always displays the latest saved snapshot (as opposed to showing the “list of dashboards”). This app does not implement any kind of access control for dashboards, but could be used as a base from which to add these features.
* `minimal/`
  * This sample application is the absolute minimal example of how to use Dashboard Engine. This app contains only a DashboardCanvas component, connected to a single hardcoded sample data frame. Users of this app can configure the canvas how they like, but their changes are not visible to any other user, and are lost when the user closes the tab/window or navigates away.
* `multi_dashboard/`
  * This sample application shows how to use Dashboard Engine in conjunction with Snapshot Engine to allow users not only to create and edit their own dashboards, but persist them on the server for later retrieval by themselves and other users. This app also shows the functioning of the connection_params mechanism for an instance of the dashboard engine to potentially connect to multiple data sources, as configured outside the canvas. This app does not implement any kind of access control for dashboards, but could be used as a base from which to add these features.
* `preloaded/`
  * This sample application shows how to preload a DashboardCanvas with an arrangement of elements, either as a way of building a non-user-editable app using Dashboard Engine, or as a way of providing an initial state for a canvas, for users to then modify.
