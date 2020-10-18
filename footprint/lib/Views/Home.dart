import 'package:curved_navigation_bar/curved_navigation_bar.dart';
import 'package:flutter/material.dart';
import 'package:footprint/Views/LandingPage.dart';

class Home extends StatefulWidget {
  @override
  _HomeState createState() => _HomeState();
}

class _HomeState extends State<Home> {
  int _page = 1;
  PageController _control = PageController();
  Color backColor = Color.fromRGBO(41, 41, 41, 1);

  @override
  void initState() {
    super.initState();
    _control = PageController(
      initialPage: 1,
      keepPage: true,
      viewportFraction: 1,
    );
  }

  @override
  void dispose() {
    _control.dispose();
    super.dispose();
  }

  void onPageChanged(int page) {
    setState(() {
      this._page = page;
      navigationTapped(_page);
    });
  }

  void navigationTapped(int page) {
    //Animating Page
    _control.jumpToPage(page);
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      bottomNavigationBar: CurvedNavigationBar(
        index: _page,
        onTap: navigationTapped,
        backgroundColor: Colors.grey,
        height: 60,
        items: [
          Icon( Icons.home, size: 30, color: Colors.black, ),
          Icon( Icons.pin_drop, size: 30, color: Colors.black, ),
          Icon( Icons.person, size: 30, color: Colors.black, ),
        ],
      ),

      body: PageView(
        controller: _control,
        onPageChanged: onPageChanged,
        children: [
          Landing(),
          Container(
            color: Colors.deepPurple,
          ),
          Container(
            color: Colors.indigoAccent,
          ),
        ],
      ),
    );
  }
}
