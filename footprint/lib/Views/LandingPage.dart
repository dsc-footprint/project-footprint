import 'package:flutter/material.dart';

import 'package:horizontal_card_pager/horizontal_card_pager.dart';
import 'package:horizontal_card_pager/card_item.dart';

//demo for the horizontal slider of maps i'd like to add
class Landing extends StatefulWidget {
  @override
  _LandingState createState() => _LandingState();
}

class _LandingState extends State<Landing> {
  @override
  @override
  Widget build(BuildContext context) {
    List<CardItem> items = [
      IconTitleCardItem(
        text: "Alarm",
        iconData: Icons.access_alarms,
      ),
      IconTitleCardItem(
        text: "Add",
        iconData: Icons.add,
      ),
      IconTitleCardItem(
        text: "Call",
        iconData: Icons.add_call,
      ),
      IconTitleCardItem(
        text: "WiFi",
        iconData: Icons.wifi,
      ),
      IconTitleCardItem(
        text: "File",
        iconData: Icons.attach_file,
      ),
      IconTitleCardItem(
        text: "Air Play",
        iconData: Icons.airplay,
      ),
    ];
    return MaterialApp(
      home: Scaffold(
        backgroundColor: Colors.grey,
        body: SafeArea(
          child: ListView(
            children: [
              Container(
                height: MediaQuery.of(context).size.height / 2,
                child: Column(
                  children: [
                    Text("OH HI MARK, FANCY SEEING YOU HERE"),
                    Container(
                      child: HorizontalCardPager(
                        items: items,
                      ),
                    ),
                  ],
                ),
              ),
              Container(
                height: MediaQuery.of(context).size.height / 2,
                child: Column(
                  children: [
                    Text("OH HI MARK, FANCY SEEING YOU HERE"),
                    Container(
                      child: HorizontalCardPager(
                        items: items,
                      ),
                    ),
                  ],
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
