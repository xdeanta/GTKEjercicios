import gi
gi.require_version("Gtk","3.0")

from gi.repository import Gtk

class GtkTreeView(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self,title = "TreeView")
        self.set_size_request(400,300)
        cajaP = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL, spacing=4)
        cajaT1 = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing=4)
        cajaT2 = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing=4)
        cajaBtn = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing=4)
        self.btnAgregar = Gtk.Button(label="Agregar >")
        #self.btnAgregar.connect("clicked", self.on_btnAgregar_clicked)
        self.btnEliminar = Gtk.Button(label="< Eliminar")
        #self.btnAgregar.connect("clicked", self.on_btnEliminar_clicked)

        cajaBtn.pack_start(self.btnAgregar, False, False, 50)
        cajaBtn.pack_start(self.btnEliminar, False, False, 2)

        modeloTabla1 = Gtk.ListStore(str)

        modeloTabla1.append(["xavier"])
        modeloTabla1.append(["javier"])
        modeloTabla1.append(["jose"])
        modeloTabla1.append(["ana"])

        self.filtrado = "None"
        filtro_nombres = modeloTabla1.filter_new()
        filtro_nombres.set_visible_func(self.filtrado_nombre)

        cellRenderer = Gtk.CellRendererText()
        cellRenderer.props.editable = False

        self.tabla1 = Gtk.TreeView(model=modeloTabla1)
        columna = Gtk.TreeViewColumn("Nombre")
        columna.pack_start(cellRenderer,False)
        columna.add_attribute(cellRenderer,"text",0)
        self.tabla1.append_column(columna)


        scroll = Gtk.ScrolledWindow()
        scroll.add(self.tabla1)
        scroll.set_policy(Gtk.PolicyType.NEVER,Gtk.PolicyType.AUTOMATIC)

        cajaBusqueda = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL,spacing = 2)
        lblBusqueda = Gtk.Label(label="Buscar")
        self.txtBusqueda = Gtk.Entry()
        cajaBusqueda.pack_start(lblBusqueda,False,False,2)
        cajaBusqueda.pack_start(self.txtBusqueda,True,True,2)

        self.btnLimpiar = Gtk.Button(label="Limpiar")
        self.btnLimpiar2 = Gtk.Button(label="Limpiar")

        cajaT1.pack_start(scroll,True, True, 2)
        cajaT1.pack_start(cajaBusqueda,True,False,2)
        cajaT1.pack_start(self.btnLimpiar,False, False, 2)

        modeloTabla2 = Gtk.ListStore(str)


        cellRenderer2 = Gtk.CellRendererText()
        cellRenderer.props.editable = False

        self.tabla2 = Gtk.TreeView(model=modeloTabla2)
        columna = Gtk.TreeViewColumn("Nombre")
        columna.pack_start(cellRenderer2, False)
        columna.add_attribute(cellRenderer2, "text", 0)
        self.tabla2.append_column(columna)

        scroll2 = Gtk.ScrolledWindow()
        scroll2.add(self.tabla2)
        scroll2.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)

        cajaBusqueda2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=2)
        lblBusqueda = Gtk.Label(label="Buscar")
        self.txtBusqueda2 = Gtk.Entry()
        cajaBusqueda2.pack_start(lblBusqueda, False, False, 2)
        cajaBusqueda2.pack_start(self.txtBusqueda2, True, True, 2)


        cajaT2.pack_start(scroll2, True, True, 2)
        cajaT2.pack_start(cajaBusqueda2, True, False, 2)
        cajaT2.pack_start(self.btnLimpiar2, False, False, 2)

        #cajaT2.pack_start(scroll2, False, True, 2)

        cajaP.pack_start(cajaT1,True,True,5)
        cajaP.pack_start(cajaBtn,False, True,4)
        cajaP.pack_start(cajaT2, True, True, 10)

        seleccion = self.tabla1.get_selection()
        seleccion2 = self.tabla2.get_selection()
        seleccion.connect("changed", self.on_seleccion_changed)
        self.btnAgregar.connect("clicked", self.on_btnAgregar_clicked, seleccion)
        self.btnEliminar.connect("clicked", self.on_btnEliminar_clicked, seleccion2)
        self.btnLimpiar.connect("clicked", self.on_btnLimpiar_clicked)
        self.btnLimpiar2.connect("clicked", self.on_btnLimpiar2_clicked)
        self.txtBusqueda.connect("insert-at-cursor", self.on_txtBusqueda_changed,)


        self.add(cajaP)

        self.connect("delete-event", Gtk.main_quit)
        self.show_all()


    def on_seleccion_changed(self,seleccion):
        """ aaaa """

    def on_btnAgregar_clicked(self, boton, seleccion):
        modelo, fila = seleccion.get_selected()
        modelo2 = self.tabla2.get_model()
        tupla = []

        if fila is not None:
            tupla.append(modelo[fila][0])
            #print(tupla)
            modelo2.append(tupla)
            modelo.remove(fila)

    def on_btnEliminar_clicked(self, boton, seleccion):
        modelo, fila = seleccion.get_selected()
        modelo2 = self.tabla1.get_model()
        tupla = []

        if fila is not None:
            tupla.append(modelo[fila][0])
            #print(tupla)
            modelo2.append(tupla)
            modelo.remove(fila)

    def on_btnLimpiar_clicked(self,boton):
        self.txtBusqueda.set_text("")

    def on_btnLimpiar2_clicked(self,boton):
        self.txtBusqueda2.set_text("")

    def on_txtBusqueda_changed(self,txtBusqueda):
        """TODO"""

    def filtrado_nombre(self,modelo,fila, datos):
        if(self.filtrado is None or self.filtrado == "None"):
            return True
        else:
            return modelo[fila][0] == self.filtrado


if __name__ == "__main__":
    GtkTreeView()

    Gtk.main()

